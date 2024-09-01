import { Injectable, Inject, PLATFORM_ID } from '@angular/core';
import { isPlatformBrowser, isPlatformServer } from '@angular/common';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { makeStateKey, TransferState } from '@angular/core';
import { environment } from '../environment/environment';
import { Observable, of, tap, catchError, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private apiUrl: string = "";

  constructor(
    private http: HttpClient,
    private transferState: TransferState,
    @Inject(PLATFORM_ID) private platformId: Object
  ) {
    if (isPlatformServer(this.platformId)) {
      this.apiUrl = environment.serverApiUrl;
    } else if (isPlatformBrowser(this.platformId)) {
      this.apiUrl = environment.clientApiUrl;
    }
  }

  getApiUrl(): string {
    return this.apiUrl;
  }

  // generic get method to fetch data from the server with caching
  get<T>(route: string): Observable<T> {
    //make a state key for this data
    const STATE_KEY = makeStateKey<T>(route);

    //if there already exists a state key
    if (this.transferState.hasKey(STATE_KEY)) {
      // get the cached data or null if there is none
      const data = this.transferState.get<T | null>(STATE_KEY, null);
      // remove the key to avoid memory leaks
      this.transferState.remove(STATE_KEY);
      // if there is cached data, return it as an observable
      if (data !== null) {
        return of(data);
      }
    }
    // if there wasn't a state key or there was no data cached, make a request to the server
    return this.http.get<T>(this.apiUrl + route).pipe(
      // cache the data received from the server
      tap(data => {
        if (isPlatformServer(this.platformId)) {
          this.transferState.set(STATE_KEY, data);
        }
      }),
      // handle any errors that may occur
      catchError(this.handleError)
    );
  }

  private handleError(err: HttpErrorResponse): Observable<never> {
    let errorMessage = '';
    console.error(err);
    if (err.error instanceof ErrorEvent) {
      // A client-side or network error occurred. Handle it accordingly.
      errorMessage = `An error occurred: ${err.error.message}`;
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong,
      errorMessage = `Server returned code: ${err.status}, error message is: ${err.message}`;
    }
    console.error(errorMessage);
    return throwError(() => errorMessage);
  }
}
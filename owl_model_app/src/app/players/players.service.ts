import { Injectable, Inject, PLATFORM_ID } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { makeStateKey, TransferState } from '@angular/core';
import { Observable, of, tap, catchError, throwError } from 'rxjs';
import { IPlayer } from "./player";
import { ApiService } from "../api.service";

@Injectable({
  providedIn: 'root'
})
export class PlayersService {
  private apiUrl: string;

  constructor(private http: HttpClient, private apiService: ApiService) {
    this.apiUrl = apiService.getApiUrl();
    console.log(this.apiUrl);
   }
}

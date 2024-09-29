import { TuiRoot } from "@taiga-ui/core";
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { RouterModule } from '@angular/router';
import { MatToolbarModule} from '@angular/material/toolbar';
import { TuiButton, tuiButtonOptionsProvider } from '@taiga-ui/core';
import { MatIconModule } from '@angular/material/icon';
import { MatSidenavModule } from '@angular/material/sidenav';
import {TuiButtonClose} from '@taiga-ui/kit';
import {MatListModule} from '@angular/material/list';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterModule, TuiRoot, MatToolbarModule, RouterModule, TuiButton, MatIconModule, MatSidenavModule, TuiButtonClose, MatListModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  providers: [tuiButtonOptionsProvider({size: 'm'})],
})
export class AppComponent {
  title = 'owl_model_app';
}

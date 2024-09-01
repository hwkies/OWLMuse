import { Component } from '@angular/core';
import { MatToolbarModule} from '@angular/material/toolbar';
import { RouterModule } from '@angular/router';
import {TuiButton} from '@taiga-ui/core';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [MatToolbarModule, RouterModule, TuiButton],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {

}

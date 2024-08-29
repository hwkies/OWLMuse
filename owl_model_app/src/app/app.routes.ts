import { Routes } from '@angular/router';
import { PlayersComponent } from './players/players.component';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';


const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    title: 'Home'
  },
  {
    path: 'players',
    component: PlayersComponent,
    title: 'Player Win Rates'
  }
];

export default routes;

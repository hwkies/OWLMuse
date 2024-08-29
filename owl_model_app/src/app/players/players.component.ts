import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { PlayersService } from './players.service';
import { IPlayer } from "./player";
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-players',
  standalone: true,
  imports: [CommonModule, HttpClientModule, RouterModule],
  templateUrl: './players.component.html',
  styleUrl: './players.component.css'
})
export class PlayersComponent implements OnInit {
  pageTitle : string = 'Player Win Rates';
  errorMessage : string = '';
  players : IPlayer[] = [];

  constructor(private route: ActivatedRoute,
              private router: Router,
              private playersService: PlayersService) {
  }

  ngOnInit(): void {
    this.getPlayers();
  }

  getPlayers(): void {
    this.playersService.getPlayerWinRates().subscribe({
      next: players => {
        this.players = players;
      },
      error: err => {
        this.errorMessage = err;
      }
    });
  }

//   onBack(): void {
//     this.router.navigate(['/products']);
//   }
}
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';

import {Home} from './home/home';
import {MovieList} from './movie-list/movie-list';
import { FormsModule } from '@angular/forms';
@Component({
  selector: 'app-root',
  imports: [RouterOutlet, HttpClientModule, HttpClientXsrfModule, FormsModule, Home, MovieList],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  protected title = 'front';
}

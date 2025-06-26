import { Routes } from '@angular/router';
import {Home} from './home/home';
import {MovieList} from './movie-list/movie-list';

const routeConfig: Routes = [
  {
    path: '',
    component: Home,
    title: 'Home page',
  },
  {
    path: 'movie_list',
    component: MovieList,
    title: 'Movie List',
  },
];
export default routeConfig;
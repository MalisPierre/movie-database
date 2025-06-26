import { Component, ViewChild, ElementRef } from '@angular/core';
import { ApiService } from '../api-service';
import { ChangeDetectorRef } from '@angular/core';
import { SrvRecord } from 'dns';
import { BlockList } from 'net';

@Component({
  selector: 'app-movie-list',
  imports: [],
  templateUrl: './movie-list.html',
  styleUrl: './movie-list.scss',
})
export class MovieList {

  
  data: any[] = [];
  errorMessage: string = "";

  constructor(private cdRef: ChangeDetectorRef, private apiService: ApiService) {}
    ngOnInit(): void {
      this.cdRef.detectChanges();
    }

  search(publishedDateStart: HTMLInputElement, publishedDateEnd: HTMLInputElement, statussesElement: Array<HTMLInputElement>, genresElement: Array<HTMLInputElement>): void {
    this.data = []
    this.errorMessage = ""
    let genres = []
    let statusses = []
    
    if (statussesElement[0].checked)
      statusses.push("in_development")
    if (statussesElement[1].checked)
      statusses.push("in_production")
    if (statussesElement[2].checked)
      statusses.push("published")
    if (statussesElement[3].checked)
      statusses.push("cancelled")
    
    if (genresElement[0].checked)
      genres.push("horror")
    if (genresElement[1].checked)
      genres.push("western")
    if (genresElement[2].checked)
      genres.push("mafia")
    if (genresElement[3].checked)
      genres.push("fantasy")
    if (genresElement[4].checked)
      genres.push("sci-fi")
    if (genresElement[5].checked)
      genres.push("historic")
    if (genresElement[6].checked)
      genres.push("cartoon")
    if (genresElement[7].checked)
      genres.push("comedy")

    this.apiService.getMovies(publishedDateStart.value, publishedDateEnd.value, genres, statusses).subscribe(
      (data) => {
        this.errorMessage = ""
        this.data = data;
        this.cdRef.detectChanges();
      },
      (error) => {
        if (error.status == 404)
        {
          this.errorMessage = "aucun film trouvé"
          this.data = []
          this.cdRef.detectChanges();
        }
        else {
        this.errorMessage = JSON.stringify("Erreur: " + error.status + " " + error.statusText);
        this.data = []
        this.cdRef.detectChanges();
        }

      }
    );
  }

}

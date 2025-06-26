import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private baseUrl = 'http://127.0.0.1:8000'; // Example API URL
  constructor(private http: HttpClient) {}
  // Get all posts
  getMovies(publishedDateStart: string, publishedDateEnd: string, genres: Array<string>, status: Array<string>): Observable<any> {
    
    let post = {
      'publishedDateStart': publishedDateStart,
      'publishedDateEnd': publishedDateEnd,
      'genre': genres,
      'status': status,
    }
    return this.http.post(`${this.baseUrl}/movie/read/`, post);
  }
  // Get a single post by ID
  // getPostById(id: number): Observable<any> {
  //   return this.http.get(`${this.baseUrl}/posts/${id}`);
  // }
  // // Create a new post
  // createPost(post: any): Observable<any> {
  //   return this.http.post(`${this.baseUrl}/posts`, post);
  // }
  // // Update a post
  // updatePost(id: number, post: any): Observable<any> {
  //   return this.http.put(`${this.baseUrl}/posts/${id}`, post);
  // }
  // // Delete a post
  // deletePost(id: number): Observable<any> {
  //   return this.http.delete(`${this.baseUrl}/posts/${id}`);
  // }
}
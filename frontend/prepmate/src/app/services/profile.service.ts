import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({ providedIn: 'root' })
export class ProfileService {
  private baseUrl = environment.apiUrl + '/profile';

  constructor(private http: HttpClient) {}

  createProfile(data: any): Observable<any> {
    return this.http.post(this.baseUrl, data);
  }

  updateProfile(data: any): Observable<any> {
    return this.http.put(this.baseUrl, data);
  }

  getProfile(): Observable<any> {
    return this.http.get(this.baseUrl);
  }
}

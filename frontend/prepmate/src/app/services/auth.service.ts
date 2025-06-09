import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { TokenService } from './token.service';

export interface AuthResponse {
  access_token: string;
  student: any;
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private baseUrl = environment.apiUrl + '/auth';

  constructor(private http: HttpClient, private tokenService: TokenService) {}

  login(data: { email: string; password: string }): Observable<AuthResponse> {
    return this.http.post<AuthResponse>(`${this.baseUrl}/login`, data);
  }

  signup(data: any): Observable<AuthResponse> {
    return this.http.post<AuthResponse>(`${this.baseUrl}/signup`, data);
  }

  setToken(token: string) {
    this.tokenService.setToken(token);
  }

  removeToken() {
    this.tokenService.removeToken();
  }

  getToken(): string | null {
    return this.tokenService.getToken();
  }
}

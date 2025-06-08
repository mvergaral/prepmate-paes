import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { AuthResponse } from '../services/auth.service';
import { TokenService } from '../services/token.service';

export interface SessionState {
  token: string | null;
  user: any | null;
}

@Injectable({ providedIn: 'root' })
export class AuthStore {
  private state: SessionState = {
    token: null,
    user: null
  };

  private tokenSubject = new BehaviorSubject<string | null>(this.state.token);
  token$ = this.tokenSubject.asObservable();

  private userSubject = new BehaviorSubject<any | null>(this.state.user);
  user$ = this.userSubject.asObservable();

  constructor(private tokenService: TokenService) {
    const savedToken = this.tokenService.getToken();
    const savedUser = localStorage.getItem('user');
    if (savedToken) {
      this.state.token = savedToken;
      this.tokenSubject.next(savedToken);
    }
    if (savedUser) {
      this.state.user = JSON.parse(savedUser);
      this.userSubject.next(this.state.user);
    }
  }

  setSession(res: AuthResponse) {
    this.state = { token: res.access_token, user: res.student };
    this.tokenService.setToken(this.state.token || '');
    localStorage.setItem('user', JSON.stringify(this.state.user));
    this.tokenSubject.next(this.state.token);
    this.userSubject.next(this.state.user);
  }

  clear() {
    this.state = { token: null, user: null };
    this.tokenService.removeToken();
    localStorage.removeItem('user');
    this.tokenSubject.next(null);
    this.userSubject.next(null);
  }
}

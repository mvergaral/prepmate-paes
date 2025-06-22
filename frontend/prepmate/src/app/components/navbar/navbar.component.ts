import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthStore } from '../../store/auth.store';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
  standalone: false
})
export class NavbarComponent {
  menuOpen = false;
  token$ = this.store.token$;

  constructor(private store: AuthStore, private router: Router) {}

  toggleMenu() {
    this.menuOpen = !this.menuOpen;
  }

  logout() {
    this.store.clear();
    this.menuOpen = false;
    this.router.navigate(['/home']);
  }
}

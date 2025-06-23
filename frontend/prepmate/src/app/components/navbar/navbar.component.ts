import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthStore } from '../../store/auth.store';
import { ThemeService } from '../../services/theme.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
  standalone: false
})
export class NavbarComponent {
  menuOpen = false;
  token$ = this.store.token$;
  isDark = false;

  constructor(
    private store: AuthStore,
    private router: Router,
    private theme: ThemeService
  ) {
    this.isDark = this.theme.isDarkMode();
  }

  toggleMenu() {
    this.menuOpen = !this.menuOpen;
  }

  toggleDarkMode() {
    this.theme.toggleTheme();
    this.isDark = this.theme.isDarkMode();
  }

  logout() {
    this.store.clear();
    this.menuOpen = false;
    this.router.navigate(['/home']);
  }
}

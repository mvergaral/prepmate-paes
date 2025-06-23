import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ThemeService } from '../services/theme.service';
import { TokenService } from '../services/token.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.page.html',
  styleUrls: ['./home.page.scss'],
  standalone: false
})
export class HomePage implements OnInit {
  isDark = false;

  constructor(
    private theme: ThemeService,
    private tokenService: TokenService,
    private router: Router,
  ) {
    this.isDark = this.theme.isDarkMode();
  }

  ngOnInit() {
    const token = this.tokenService.getToken();
    if (token) {
      this.router.navigate(['/dashboard']);
    }
  }

  toggleDarkMode() {
    this.theme.toggleTheme();
    this.isDark = this.theme.isDarkMode();
  }
}

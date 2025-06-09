import { Component } from '@angular/core';
import { ThemeService } from '../services/theme.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.page.html',
  styleUrls: ['./home.page.scss'],
  standalone: false
})
export class HomePage {
  isDark = false;

  constructor(private theme: ThemeService) {
    this.isDark = this.theme.isDarkMode();
  }

  toggleDarkMode() {
    this.theme.toggleTheme();
    this.isDark = this.theme.isDarkMode();
  }
}
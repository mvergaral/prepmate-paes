import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.page.html',
  styleUrls: ['./home.page.scss'],
  standalone: false
})
export class HomePage {
  isDark = false;

  constructor() {
    this.isDark = document.documentElement.classList.contains('dark');
  }

  toggleDarkMode() {
    this.isDark = !this.isDark;
    const html = document.documentElement;
    if (this.isDark) {
      html.classList.add('dark');
    } else {
      html.classList.remove('dark');
    }
    localStorage.setItem('theme', this.isDark ? 'dark' : 'light');
  }
}
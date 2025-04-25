import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ThemeService {
  private darkClass = 'dark';

  constructor() {
    this.initTheme();
  }

  initTheme() {
    const saved = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (saved === 'dark' || (!saved && prefersDark)) {
      document.documentElement.classList.add(this.darkClass);
    } else {
      document.documentElement.classList.remove(this.darkClass);
    }
  }

  toggleTheme() {
    const html = document.documentElement;
    const isDark = html.classList.contains(this.darkClass);

    if (isDark) {
      html.classList.remove(this.darkClass);
      localStorage.setItem('theme', 'light');
    } else {
      html.classList.add(this.darkClass);
      localStorage.setItem('theme', 'dark');
    }
  }

  isDarkMode(): boolean {
    return document.documentElement.classList.contains(this.darkClass);
  }
}
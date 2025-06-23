import { Component, OnInit } from '@angular/core';
import { ThemeService } from './services/theme.service';
import { AuthStore } from './store/auth.store';
import { NotificationService } from './services/notification.service';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
  standalone: false,
})
export class AppComponent implements OnInit {
  constructor(
    private themeService: ThemeService,
    private store: AuthStore,
    private notifications: NotificationService
  ) {}

  ngOnInit() {
    this.store.token$.subscribe(token => {
      if (token) {
        this.notifications.fetch();
      }
    });
  }
}

import { Component } from '@angular/core';
import { NotificationService } from '../../services/notification.service';

@Component({
  selector: 'app-notification-banner',
  templateUrl: './notification-banner.component.html',
  styleUrls: ['./notification-banner.component.scss'],
  standalone: false
})
export class NotificationBannerComponent {
  message$ = this.notification.message$;

  constructor(private notification: NotificationService) {}

  close() {
    this.notification.clear();
  }
}

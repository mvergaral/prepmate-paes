import { Component } from '@angular/core';
import { ErrorService } from '../../services/error.service';

@Component({
  selector: 'app-error-banner',
  templateUrl: './error-banner.component.html',
  styleUrls: ['./error-banner.component.scss'],
  standalone: false
})
export class ErrorBannerComponent {
  message$ = this.error.message$;

  constructor(private error: ErrorService) {}

  close() {
    this.error.clear();
  }
}

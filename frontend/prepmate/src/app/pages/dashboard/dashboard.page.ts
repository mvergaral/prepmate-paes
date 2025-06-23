import { Component, OnInit } from '@angular/core';
import { ProgressService, SubjectProgress } from '../../services/progress.service';
import { AuthStore } from '../../store/auth.store';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.page.html',
  styleUrls: ['./dashboard.page.scss'],
  standalone: false
})
export class DashboardPage implements OnInit {
  progress: SubjectProgress[] = [];
  total = 0;
  correct = 0;

  constructor(private progressService: ProgressService, private store: AuthStore) {}

  ngOnInit() {
    const user = this.store['state'].user;
    this.progressService.getProgress(user.id).subscribe(res => {
      this.progress = res.progress;
      this.total = this.progress.reduce((acc, p) => acc + p.total, 0);
      this.correct = this.progress.reduce((acc, p) => acc + p.correct, 0);
    });
  }

  get overallPercent() {
    return this.total ? this.correct / this.total : 0;
  }

  iconFor(subject: string) {
    const name = subject.toLowerCase();
    if (name.includes('matem')) return 'calculator-outline';
    if (name.includes('ciencia')) return 'flask-outline';
    if (name.includes('lectora')) return 'book-outline';
    if (name.includes('historia')) return 'earth-outline';
    return 'help-circle-outline';
  }
}

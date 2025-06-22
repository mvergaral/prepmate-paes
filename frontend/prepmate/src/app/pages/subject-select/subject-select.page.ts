import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SubjectService } from '../../services/subject.service';

@Component({
  selector: 'app-subject-select',
  templateUrl: './subject-select.page.html',
  styleUrls: ['./subject-select.page.scss'],
  standalone: false
})
export class SubjectSelectPage implements OnInit {
  subjects: any[] = [];

  constructor(private subjectService: SubjectService, private router: Router) {}

  ngOnInit() {
    this.subjectService.getSubjects().subscribe(res => {
      const arr = (res as any).data || res;
      this.subjects = arr.map((s: any) => ({ ...s, selected: false }));
    });
  }

  confirmSelection() {
    const selected = this.subjects.filter(s => s.selected).map(s => s.name);
    if (!selected.length) { return; }
    this.subjectService.saveSelectedSubjects(selected);
    this.router.navigate(['/exercise', selected[0]]);
  }
}

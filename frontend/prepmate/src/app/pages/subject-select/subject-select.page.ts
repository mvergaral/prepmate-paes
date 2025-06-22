import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SubjectService } from '../../services/subject.service';

@Component({
  selector: 'app-subject-select',
  templateUrl: './subject-select.page.html',
  styleUrls: ['./subject-select.page.scss']
})
export class SubjectSelectPage implements OnInit {
  subjects: any[] = [];

  constructor(private subjectService: SubjectService, private router: Router) {}

  ngOnInit() {
    this.subjectService.getSubjects().subscribe(res => (this.subjects = (res as any).data || res));
  }

  open(subject: any) {
    this.router.navigate(['/exercise', subject.name]);
  }
}

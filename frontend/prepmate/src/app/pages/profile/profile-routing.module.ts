import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ProfilePage } from './profile.page';
import { ProfileViewPage } from './profile-view/profile-view.page';

const routes: Routes = [
  {
    path: '',
    component: ProfilePage
  },
  {
    path: 'view',
    component: ProfileViewPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ProfilePageRoutingModule {}

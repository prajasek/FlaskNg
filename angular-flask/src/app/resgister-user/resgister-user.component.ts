import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-resgister-user',
  templateUrl: './resgister-user.component.html',
  styleUrls: ['./resgister-user.component.css']
})
export class ResgisterUserComponent {

  name: string = ''; 
  userName: string = '';
  password: string = '';

  constructor(private auth: AuthService) { }

  ngOnInit(): void {
  }

  onSubmit(){
    console.log('Register');
    console.log(this.userName)
    this.auth.registerUser(this.name, this.userName, this.password);

  }
}

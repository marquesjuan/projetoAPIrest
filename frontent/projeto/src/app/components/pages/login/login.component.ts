import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { IUsuario } from '../../../models/usuario.model';
import { UsuarioService } from '../../../services/usuario.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule,CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  baseUsuario: IUsuario = {email: '', senha: ''};
  constructor(private serviceUsuario: UsuarioService){

  }
  login(){
    this.serviceUsuario.getUser(this.baseUsuario.email,this.baseUsuario.senha)
    .subscribe(response => {
      console.log("ok",response);
    }, error => {
      console.log("Error", error)
    });

  }
}

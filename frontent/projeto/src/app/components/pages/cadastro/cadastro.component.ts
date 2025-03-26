import { Component } from '@angular/core';
import { IUsuario } from '../../../models/usuario.model';
import { UsuarioService } from '../../../services/usuario.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-cadastro',
  standalone:true,
  imports: [CommonModule,FormsModule],
  templateUrl: './cadastro.component.html',
  styleUrl: './cadastro.component.css'
})
export class CadastroComponent {
  cadastro: IUsuario = {nome:'' , senha: '', email: ''};
  
  constructor(private usuariocadastro: UsuarioService){}
  cadastrar(){
      this.usuariocadastro.postUser(String(this.cadastro.nome),this.cadastro.email, this.cadastro.senha)
      .subscribe(response => {
        console.log("ok", response);
      }, error => {
        console.log("error", error)
      });
  }  
}

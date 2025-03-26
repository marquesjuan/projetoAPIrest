import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {
  
  private apiUrl = 'http://localhost:8000/usuario/login'
  private apiUrlCadastro = 'http://localhost:8000/usuario/cadastro'
  
  constructor(private __httpclient: HttpClient) {
   }

   getUser(email: string , senha: string): Observable<any> {
    return this.__httpclient.get<any>(`${this.apiUrl}?email=${email}&senha=${senha}`);
   }

   postUser(nome: string, email: string, senha: string): Observable<any>{
    const body = {nome, email, senha};
    return this.__httpclient.post<any>(this.apiUrlCadastro, body);
   }

}

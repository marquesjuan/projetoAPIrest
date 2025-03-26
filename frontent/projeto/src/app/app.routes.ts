import { Routes } from '@angular/router';
import { LoginComponent } from './components/pages/login/login.component';
import { CadastroComponent } from './components/pages/cadastro/cadastro.component';
export const routes: Routes = [
    {path:"login" , component:LoginComponent},
    {path:"cadastro", component:CadastroComponent}
];

import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { routerTransition } from '../router.animations';
import {LoginService} from '../shared/services/login.service';

@Component({
    selector: 'app-login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.scss'],
    providers: [LoginService],
    animations: [routerTransition()]
})
export class LoginComponent implements OnInit {
    input;

    constructor(
        private loginService: LoginService
    ) {
    }
    ngOnInit() {
        this.input = {
            email: '',
            password: ''
        };
    }

    loginUser() {
        console.log(this.input, 'trelemorelebumcycyk');
        this.loginService.loginUser(this.input).subscribe(
            response => {
                localStorage.setItem('isLoggedin', 'true');
                console.log(response);
                alert('User' + this.input.email + ' logged');
            },
            error =>  {
                console.log('ERROR', error);
            }
        );

    }
}

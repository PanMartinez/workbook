import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  baseurl =  'http://localhost:8000/api';
  // httpHeaders = new HttpHeaders({'Content-type': 'application/json'});
  constructor(private http: HttpClient) { }

  loginUser(userData): Observable<any> {
    return this.http.post(this.baseurl + '/token/', userData);

  }
}

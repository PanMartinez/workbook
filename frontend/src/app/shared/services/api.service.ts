import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  baseurl = 'http://localhost:8000';
  constructor() { }
}


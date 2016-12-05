import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

import { RoutingModule } from './app.routing.module';

import { AppComponent } from './app.component';
import { HeroComponent } from './hero.component';

import { HeroService } from './hero.service';

@NgModule({
    imports: [BrowserModule, FormsModule, RouterModule, RoutingModule],
    declarations: [AppComponent, HeroComponent],
    providers: [HeroService],
    bootstrap: [AppComponent]
})
export class AppModule { }

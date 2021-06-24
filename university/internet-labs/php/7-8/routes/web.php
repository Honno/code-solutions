<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('hello', function () {
    return 'Hello World!';
});

Route::get('list', 'AccountController@list');
Route::get('show/{id}', 'AccountController@show');

Auth::routes();

Route::get('/home', 'HomeController@index')->name('home');

Route::get('display',
           'AccountController@display')->name('display_account');

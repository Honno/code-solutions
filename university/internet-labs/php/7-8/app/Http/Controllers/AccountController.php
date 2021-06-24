<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Account;

use Gate;

class AccountController extends Controller {

    public function display() {
        $accountsQuery = Account::all();
        if (Gate::denies('displayall')) {
            $accountsQuery=$accountsQuery->where('userid', auth()->user()->id);
        }
        return view('/display', array('accounts'=>$accountsQuery));
    }

    public function show($id) {
        $account = Account::find($id);
        return view('/show', array('account' => $account));
    }

    public function list() {
        return view('/list', array('accounts'=>Account::all()));
    }
}

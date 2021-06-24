<table>
    <thead>
        <tr>
            <th> id</th>
            <th> Account no</th>
            <th> Type </th>
            <th> balance </th>
            <th> Interest</th>
            <th> created_on </th>
        </tr>
    </thead>
    <tbody>
        @foreach($accounts as $account)
        <tr>
            <td> {{$account->id}} </td>
            <td> {{$account->type}} </td>
            <td> {{$account->accountno}} </td>
            <td> {{$account->balance}} </td>
            <td> {{$account->interest}} </td>
            <td> {{$account->created_on}} </td>
        </tr>
        @endforeach
    </tbody>
</table>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Books</title>
</head>
<body>
    <h1>Books</h1>
    <table>
        <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Genre</th>
        </tr>
        % for book in books:
        <tr>
            <td>{{ book[0] }}</td>
            <td>{{ book[1] }}</td>
            <td>{{ book[2] }}</td>
        </tr>
        % end
    </table>
</body>
</html>

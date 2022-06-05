//async function post_visitor() {
//    try {
//        let response = await fetch('https://tkn8j97oy9.execute-api.us-east-1.amazonaws.com/Prod/visitor_count', {
//            method: 'POST',
//            headers: {
//                //'x-api-key': '91P74Jtwbq5YJLJBJTElz6KxTXYotead9YQY9EvM'
//            }
//        });
//        let data = await response.json()
//        //console.log(data);
//        return data;
//    } catch (err) {
//        console.error(err);
//    }
//}

// GET API REQUEST
async function get_visitors() {
    // call post api request function
    // await post_visitor();
    try {
        let response = await fetch('https://tkn8j97oy9.execute-api.us-east-1.amazonaws.com/Prod/visitor_count', {
            method: 'GET',
            headers: {
                //'x-api-key': '91P74Jtwbq5YJLJBJTElz6KxTXYotead9YQY9EvM',
            }
        });
        let data = await response.json()
        document.getElementById("visitor_count").innerHTML = data.body
        console.log(data);
        return data;
    } catch (err) {
        console.error(err);
    }
}

get_visitors();

db.createUser({
    user: "sudo_admin",
    pwd: "password",
    roles: [
        {
            role: "readWrite",

            db: "allUsers",


        },
    ],
});

db.createCollection("users");
db.users.insertMany([{
    "id": 1,
    "name": "Max Svensson",
    "email": "me@gmail.com",
    "avatar": "https://robohash.org/ametveldolorem.png?size=50x50&set=set1",
    "username": "emclinden0",
    "password": "lC2)Pug$Dsq*8b|6"
},
{
    "id": 2,
    "name": "Jarl Svensson",
    "email": "js@gmail.com",
    "avatar": "https://robohash.org/quidemvelitut.png?size=50x50&set=set1",
    "username": "tjewar1",
    "password": "tO6(.zfUWLjNVF"
},
{
    "id": 3,
    "name": "Harisha Svensson",
    "email": "hs@gmail.com",
    "avatar": "https://robohash.org/harumdelectusratione.png?size=50x50&set=set1",
    "username": "akamen2",
    "password": "dP7(kp,/uW?'(j"
},
{
    "id": 4,
    "name": "Dennis Svensson",
    "email": "ds@gmail.com",
    "avatar": "https://robohash.org/asperioresipsamitaque.png?size=50x50&set=set1",
    "username": "sgwyneth5",
    "password": "jT7`pjwWNiT.C",
{
    "id": 5,
    "name": "Simon Svensson",
    "email": "ss@gmail.com",
    "avatar": "https://robohash.org/commodisimiliquesunt.png?size=50x50&set=set1",
    "username": "cmor3",
    "password": "uK6+bn46xMPfO#j"
},
{
    "id": 6,
    "name": "Zoreh Svensson",
    "email": "zs@gmail.com",
    "avatar": "https://robohash.org/vitaeporroid.png?size=50x50&set=set1",
    "username": "rporker4",
    "password": "yR7mZ*4eBKXl"
}

]);

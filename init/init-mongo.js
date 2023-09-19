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
    id: 1,
    name: "Max Svensson",
    email: "me@gmail.com"
},
{
    id: 2,
    name: "Jarl Svensson",
    email: "js@gmail.com"
},
{
    id: 3,
    name: "Harisha Svensson",
    email: "hs@gmail.com",
},
{
    id: 4,
    name: "Dennis Svensson",
    email: "ds@gmail.com",
},
{
    id: 5,
    name: "Simon Svensson",
    email: "ss@gmail.com",
},
{
    id: 6,
    name: "Zoreh Svensson",
    email: "zs@gmail.com",
}

]);


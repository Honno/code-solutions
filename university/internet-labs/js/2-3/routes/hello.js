var router = require('express').Router();

router.get('/', (req, res) => {
    res.send("Hello!");
});

router.post('/', (req, res) => {
    res.status(405).send();
});

module.exports = router;

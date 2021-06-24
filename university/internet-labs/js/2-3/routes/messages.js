var router = require('express').Router();

var messages = require('../lib/messages.js');

router.get('/', (req, res) => {
    messages.readAll(res.end);
});

router.post('/', (req, res) => {
    var msg = {
        username: req.body.username,
        text: req.body.text
    };
    messages.create(msg, res.end);
});

router.get('/:id', (req, res) => {
    messages.read(req.params.id, res.end);
});

router.put('/:id', (req, res) => {
    var msg = {
        username: req.body.username,
        text: req.body.text
    };

    messages.update(req.params.id, msg, res.end);
});

router.delete('/:id', (req, res) => {
    messages.delete(req.params.id, res.end);
});

module.exports = router;

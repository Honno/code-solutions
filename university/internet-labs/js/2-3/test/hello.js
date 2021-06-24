var chai = require('chai');
var expect = chai.expect;
var agent = require('superagent');
var status = require('http-status');

describe("Hello", () => {
    var root = "http://localhost:3001/";

    before((done) => {
        app = require('../server.js');
        app.listen(3001, () => { done(); });
    });

    it("Says hello back", (done) => {
        agent.get(root + 'hello')
            .then((res) => {
                expect(res.statusCode).to.be.equal(status.OK);
                done();
            });
    });

    it("Doesn't want anything", (done) => {
        agent.post(root + 'hello')
            .end((err, res) => {
                expect(err).to.be.an('error');
                expect(res.statusCode).to.be.equal(status.METHOD_NOT_ALLOWED);
                done();
            });
    });
});

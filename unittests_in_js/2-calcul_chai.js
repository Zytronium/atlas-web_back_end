#!/usr/bin/node
function calculateNumber(type, a, b) {
    const a_round = Math.round(a);
    const b_round = Math.round(b);

    switch (type) {
        case 'SUM':
            return a_round + b_round;
        case 'SUBTRACT':
            return a_round - b_round;
        case 'DIVIDE':
            if (b_round === 0)
                return "Error";
            return a_round / b_round;
        default:
            return "Error";
    }
}

module.exports = calculateNumber;

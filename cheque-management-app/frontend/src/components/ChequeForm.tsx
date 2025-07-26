import React, { useState } from 'react';

const ChequeForm: React.FC = () => {
    const [givenDate, setGivenDate] = useState('');
    const [bank, setBank] = useState('');
    const [chequeNumber, setChequeNumber] = useState('');
    const [amount, setAmount] = useState('');
    const [shopName, setShopName] = useState('');
    const [salesmanName, setSalesmanName] = useState('');
    const [clearDate, setClearDate] = useState('');
    const [remarks, setRemarks] = useState('');

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        const chequeDetails = {
            givenDate,
            bank,
            chequeNumber,
            amount,
            shopName,
            salesmanName,
            clearDate,
            remarks,
        };
        // Here you would typically send the chequeDetails to the backend
        console.log(chequeDetails);
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Given Date:</label>
                <input type="date" value={givenDate} onChange={(e) => setGivenDate(e.target.value)} required />
            </div>
            <div>
                <label>Bank:</label>
                <input type="text" value={bank} onChange={(e) => setBank(e.target.value)} required />
            </div>
            <div>
                <label>Cheque Number:</label>
                <input type="text" value={chequeNumber} onChange={(e) => setChequeNumber(e.target.value)} required />
            </div>
            <div>
                <label>Amount:</label>
                <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} required />
            </div>
            <div>
                <label>Shop Name:</label>
                <input type="text" value={shopName} onChange={(e) => setShopName(e.target.value)} required />
            </div>
            <div>
                <label>Salesman Name:</label>
                <input type="text" value={salesmanName} onChange={(e) => setSalesmanName(e.target.value)} required />
            </div>
            <div>
                <label>Clear Date:</label>
                <input type="date" value={clearDate} onChange={(e) => setClearDate(e.target.value)} />
            </div>
            <div>
                <label>Remarks (if bounced):</label>
                <textarea value={remarks} onChange={(e) => setRemarks(e.target.value)} />
            </div>
            <button type="submit">Submit</button>
        </form>
    );
};

export default ChequeForm;
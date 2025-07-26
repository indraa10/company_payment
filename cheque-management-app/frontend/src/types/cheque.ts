export interface ChequeDetails {
    givenDate: string;
    bank: string;
    chequeNumber: string;
    amount: number;
    shopName: string;
    salesmanName: string;
    clearDate?: string;
    remarks?: string;
}
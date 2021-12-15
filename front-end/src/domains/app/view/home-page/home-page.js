import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from "react-redux";
import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Modal from 'react-bootstrap/Modal'
import BootstrapTable from 'react-bootstrap-table-next';
import Select from 'react-select';
import { loadData, manageUpdateTables } from "../../thunks/load-data";
import { getAppClaims, } from "../../selectors";
import { Button } from "react-bootstrap";


import styles from './home-page.css';
import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';


export default function HomePage() {
    const dispatch = useDispatch();
    const claims = useSelector(getAppClaims) || {}; //access claims data from store
    const [isOpen, setIsOpen] = React.useState(false);
    
      const hideModal = () => {
        setIsOpen(false);
      };

    const columns = [
        {
            dataField: 'id',
            text: 'Id',
            hidden: true
        },
        {
            dataField: 'claim_line_item_type',
            text: 'Type'
        },
        {
            dataField: 'quantity',
            text: 'Quantity',
        },
        {
            dataField: 'decision',
            text: 'Decision',
            formatter: decisionFormatter
        },
        {
            dataField: 'amount_claimed',
            text: 'Amount Claimed',
            formatter: priceFormatter
        }];

    function decisionFormatter(cell, row, val) {
        const options = [
            { value: "approved", label: 'Approved' },
            { value: "denied", label: 'Denied' }
        ];

        if (row.decision.toLowerCase() === 'approved') {
            return (
                <Select
                    name="decision-field-select"
                    options={options}
                    defaultValue={options[0]}
                    onChange={e => handleOnChange(row, e)}
                />
            );
        }
        else {
            return (
                <Select
                    name="decision-field-select"
                    options={options}
                    defaultValue={options[1]}
                    onChange={e => handleOnChange(row, e)}
                />
            );
        }
    }

    function handleOnChange(row, e) {
        if (e.value === "approved") {
            setIsOpen(true)
            dispatch(manageUpdateTables(row, claims.data.body.data[0].id, e.value, 'approved'));
        }
        else{
            dispatch(manageUpdateTables(row, claims.data.body.data[0].id, e.value, 'denied'));
        }
    }

    function priceFormatter(cell, row) {
        return (
            <span>$ {cell.toLocaleString()} </span>
        );
    }

    //componentdidmount?
    useEffect(() => {
        dispatch(loadData());
    }, []);

    if (Object.keys(claims).length !== 0) {
        const claims_list = claims.data.body.data[0].line_items ? claims.data.body.data[0].line_items : null;
        const linkToUtilizations = "/utilization?claim_id=" + claims.data.body.data[0].id;
        return (
            <div className={styles.container}>
                <p>Customer: Paige Davenport</p>
                <p>PKN690800</p>
                <p>Claim: {claims.data.body.data[0].id}</p>

                <hr />

                <Container>
                    <Row>
                        <Col>
                            <p><b>Claim Type:</b></p>
                            <p>{claims.data.body.data[0].claim_type}</p>
                        </Col>
                        <Col><p><b>Claimed Amount:</b></p>
                            <p> $ {claims.data.body.data[0].amount_claimed.toLocaleString()}</p></Col>
                        <Col></Col>
                    </Row>
                    <Row className="claim-table-row">
                        <p style={{ marginTop: '80px' }}><b>Line Items:</b></p>
                        {
                            claims_list ? <BootstrapTable keyField="id" data={claims_list} columns={columns} /> : null
                        }
                    </Row>
                    <Row className="link-to-utilization-btn-row" style={{ float: 'right', marginRight: "0px" }}>
                        <Button href={linkToUtilizations} variant="primary" size="md" style={{ width: "150px" }}>
                            View Utilizations
                        </Button>
                    </Row>
                </Container>

                <Modal show={isOpen} onHide={hideModal}>
                    <Modal.Header>
                        <Modal.Title>Utilization Update</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>Utilization Table is being updated. Please click View Utilization button to get more info.</Modal.Body>
                    <Modal.Footer>
                        <button onClick={hideModal}>OK</button>
                    </Modal.Footer>
                </Modal>
            </div>
        );
    }
    else {
        return (
            <div className={styles.container}>

            </div>
        );
    }


}
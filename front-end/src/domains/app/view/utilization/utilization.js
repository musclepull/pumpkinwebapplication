import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from "react-redux";
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import { getUtilization } from "../../selectors";
import { loadUtilizationData } from "../../thunks/load-data";
import { Button } from "react-bootstrap";

import styles from './utilization.css';
import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';


export default function Utilization() {
    const dispatch = useDispatch();
    const utilizations = useSelector(getUtilization);
    const queryParams = new URLSearchParams(window.location.search);
    const claim_id = queryParams.get('claim_id');
    useEffect(() => {
        dispatch(loadUtilizationData(claim_id));
    }, []);

    if (utilizations !== null) {
        const linkToClaims = "/";
        return (
            <div className={styles.container}>
                <h1 style={{ color: '#0061be' }}>{utilizations.name}'s Profile</h1>
                <Row>
                    <Col>
                        <p><b>Birthday:</b></p>
                        <p>{utilizations.birthday}</p>
                    </Col>
                    <Col><p><b>Weight:</b></p>
                        <p> {utilizations.weight} lbs </p>
                    </Col>
                    <Col></Col>
                </Row>
                <h4 style={{ color: '#0061be' }}>Track Benefits</h4>
                <p style={{ marginBottom: '10px' }}><strong>Preventive Essentials Benefits</strong></p>

                <Row style={{ marginTop: '5px' }}>
                    <Col>
                        <p><b>Type:</b></p>
                    </Col>
                    <Col><p><b>Utilized:</b></p>
                    </Col>
                    <Col><p><b>Remaining:</b></p>
                    </Col>
                    <Col><p><b>Total:</b></p>
                    </Col>
                </Row>
                {
                    utilizations.utilObj.map((value, index) => {
                        return (
                            <Row key={value.row_id} style={{ marginTop: '5px' }}>
                                <Col key={value.col_id}>
                                    <p>{value.claim_line_item_type}</p>
                                </Col>
                                <Col key={value.col_id}>
                                    <p>{value.quantity}</p>
                                </Col>
                                <Col key={value.col_id}>
                                    <p>{value.remaining}</p>
                                </Col>
                                <Col key={value.col_id}>
                                    <p>{value.total}</p>
                                </Col>
                            </Row>
                        )
                    })
                }
                <Row className="link-to-claims-btn-row" style={{ float: 'right', marginRight: "0px" }}>
                    <Button href={linkToClaims} variant="primary" size="md" style={{ width: "150px" }}>
                        View Claims
                    </Button>
                </Row>



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


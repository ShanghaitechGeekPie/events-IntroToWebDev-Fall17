import React from 'react';
import ReactDOM from 'react-dom';
import { Map, Marker } from 'react-amap';
import { Button, Input } from 'antd';

const apiRoot = 'https://127.0.0.1:8090/poipath/api/v1/';
const amapApiKey = 'YOURKEY'

const boxedInfoStyle = {
    position: 'absolute',
    top: '0.2em',
    left: '0.2em',
    padding: '0.3em 0.3em 0.3em 0.3em',
    backgroundColor: '#fdfdfd',
    fontFamily: 'Microsoft YaHei UI',
    fontSize: '1.5em'
}

class NameInput extends React.Component {

    constructor() {
        super();

        this.state = {
            nameVal: ''
        }
    }
}

export default class MapDemo extends React.Component {
    
    constructor() {
        super();

        this.state = {
            center: {
                lng: 121.5960,
                lat: 31.1765
            },
            poiName: null
        };

        this.mapPlugins = ['ToolBar'];

        this.mapEvents = {
            created: (map) => {
                this.mapInstance = map;
                this.showCenter();
            },
            moveend: () => {
                this.showCenter();
            }
        };

        this.position = {
            longitude: 121.5960,
            latitude: 31.1765
        }
    }

    showCenter() {
        this.setState({
            center: this.mapInstance.getCenter()
        })
    }

    updateNameVal(e) {
        this.setState({
            poiName: e.target.value
        })
    }

    postInfo() {
        let poiInfo = {
            name: this.state.poiName,
            lng: this.state.center.lng,
            lat: this.state.center.lat
        }
        fetch(apiRoot + "poi/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(poiInfo)
        }).then(
            res => res.json()
        ).then(
            resolved => console.log(resolved)
        ).catch(
            err => console.error(err)
        );
    }

    render() {
        return (
            <Map
                amapkey={amapApiKey}
                zoom={17}
                events={this.mapEvents}
                center={this.position}
            >
                <div className="infoBox" style={boxedInfoStyle}>
                    <p>
                        当前位置：<br/>
                        经度：{this.state.center.lng}<br/>
                        纬度：{this.state.center.lat}
                    </p>
                    <Input placeholder="地点名称" onChange={this.updateNameVal.bind(this)} /><Button onClick={this.postInfo.bind(this)}>添加收藏</Button>
                </div>
                <Marker position={this.state.center}/>
            </Map>
        )
    }
}
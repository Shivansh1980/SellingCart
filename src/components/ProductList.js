import React, { Component } from 'react'
import axios from 'axios'
import './ProductListCss.css'

class ProductList extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
            products:[]
        }
    }
    componentDidMount() {
        axios.get("http://127.0.0.1:8000/api/shop/getproducts")
            .then(response => {
                console.log("your array is : ")
                console.log(response.data)

                this.setState({
                    products:response.data
                })
            })
            .catch(error => {
                console.log("This is an Error : "+error)
            })
    }
    render() {
        const { products } = this.state
        return (
            <div>
                <h1> Product available on our site : </h1>
                <table className="products">
                    <tr>
                        <th>Product name</th>
                        <th> priduct price </th>
                    </tr>
                        {
                        products.length ?
                            products.map(pr =>
                                <tr key={pr.id}>
                                    <td>{pr.product_name}</td>
                                    <td>Rs.{pr.price}</td>
                                </tr>
                            ) :
                            <h1>no object found</h1>
                        }
                </table>
            </div>    
        )
    }
}

export default ProductList

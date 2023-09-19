from fastapi import APIRouter, Response

router = APIRouter(
    prefix='/product',
    tags=['product']
)

product = ['watch', 'phone', 'laptop']


@router.get('/all')
def get_all_product():
    # return product
    data = " ".join(product)
    return Response(content=data, media_type='text/plain')


@router.get('/{id}')
def get_product_id(id: int):
    products = product[id]
    out = f"""
        <head>
        <style>
        .product {{
            width: 500px;
            height: 30px;
            border: 2px inset green;
            background-color: lightblue;
            text-align: center;
        }}
        </style>
        </head>
        <div class = "product">{products} </div>
    """
    return Response(content=out, media_type='text/html')

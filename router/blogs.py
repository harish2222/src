from fastapi import APIRouter, status, Response

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)

# creating a get method with parameter method


@router.get("/all")
def parameter_testing(para1: int = 1, para2: int = 8):
    return {"message": f"the parameter are {para1} {para2}"}


# creating a get methodd and changing the status code
@router.get("/{ids}",
            status_code=status.HTTP_200_OK,
            #  tags=["status_code", "get_methods"],
            summary="status code testing over condition",
            description="Over here we aare changing the status code according to the condition")
def status_code_ops(ids: int, response: Response):
    if (ids > 10):
        response.status_code = status.HTTP_200_OK
        return {"message": f"the ids are {ids}"}

    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"the ids are not {ids}"}

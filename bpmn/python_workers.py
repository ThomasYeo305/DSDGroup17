from datetime import date
import asyncio
import math
from camunda_orchestration_sdk import (
    CamundaAsyncClient,
    ConnectedJobContext,
    WorkerConfig,
)

def check_product_availability(
    stock_quantity,
    season_start,
    season_end,
    today=None
):
    if today is None:
        today = date.today()

    if isinstance(season_start, str):
        season_start = date.fromisoformat(season_start)

    if isinstance(season_end, str):
        season_end = date.fromisoformat(season_end)

    if season_start is None or season_end is None:
        raise ValueError("Season start and end dates are required")

    if (
        isinstance(stock_quantity, bool)
        or not isinstance(stock_quantity, (int, float))
        or not math.isfinite(stock_quantity)
        or stock_quantity < 0
    ):
        raise ValueError("Invalid stock quantity")

    if season_start > season_end:
        raise ValueError("Invalid seasonal dates")

    if stock_quantity == 0:
        return {
            "productAvailable": False,
            "availabilityReason": "Out of stock"
        }

    if today < season_start:
        return {
            "productAvailable": False,
            "availabilityReason": "Season has not started"
        }

    if today > season_end:
        return {
            "productAvailable": False,
            "availabilityReason": "Season has ended"
        }

    return {
        "productAvailable": True,
        "availabilityReason": "In season and in stock"
    }

async def request_product_correction(job: ConnectedJobContext) -> dict:
    data = job.variables.to_dict()

    listing_id = data.get("listingId", "Unknown")

    print(f"Correction requested for listing: {listing_id}")

    return {"correctionRequested": True}

async def publish_product(job: ConnectedJobContext) -> dict:
    data = job.variables.to_dict()

    product_name = data.get("productName", "Unknown Product")

    print(f"Product published: {product_name}")

    return {"listingStatus": "PUBLISHED"}

async def validate_product(job: ConnectedJobContext) -> dict:
    data = job.variables.to_dict()

    name = str(data.get("productName") or "").strip()
    description = str(data.get("productDescription") or "").strip()
    price = data.get("productPrice")
    stock = data.get("stockQuantity")
    organic = data.get("organicClaimed", False)
    certificate = str(
        data.get("organicCertificateNumber") or ""
    ).strip()

    valid = (
        bool(name)
        and bool(description)
        and type(price) in (int, float)
        and math.isfinite(price)
        and price > 0
        and type(stock) in (int, float)
        and math.isfinite(stock)
        and stock >= 0
        and float(stock).is_integer()
        and type(organic) is bool
        and (not organic or bool(certificate))
    )

    print(f"Product validation: {valid}")

    return {"productValid": valid}


async def check_seasonal_availability(job: ConnectedJobContext) -> dict:
    data = job.variables.to_dict()

    result = check_product_availability(
    stock_quantity=data.get("stockQuantity"),
    season_start=data.get("availabilityStartDate"),
    season_end=data.get("availabilityEndDate")
    )

    print(
        f"Seasonal availability: "
        f"{result['productAvailable']} - "
        f"{result['availabilityReason']}"
    )

    return result

async def set_product_available(job: ConnectedJobContext) -> dict:
    data = job.variables.to_dict()

    product_name = data.get("productName", "Unknown Product")

    print(f"{product_name} marked as AVAILABLE")

    return {
        "productStatus": "AVAILABLE"
    }


async def set_product_unavailable(job: ConnectedJobContext) -> dict:
    data = job.variables.to_dict()

    product_name = data.get("productName", "Unknown Product")
    reason = data.get("availabilityReason", "Not available")

    print(f"{product_name} marked as UNAVAILABLE: {reason}")

    return {
        "productStatus": "UNAVAILABLE"
    }

async def send_inventory_update_confirmation(
    job: ConnectedJobContext
) -> dict:
    data = job.variables.to_dict()
    product_name = data.get("productName", "Unknown Product")

    print(
        f"Inventory update confirmation sent for {product_name}"
    )

    return {"inventoryConfirmationSent": True}

async def main():
    async with CamundaAsyncClient(configuration={"CAMUNDA_LOAD_ENVFILE": "true"}) as client:
        client.create_job_worker(
            config=WorkerConfig(
                job_type="validate-product",
                job_timeout_milliseconds=30000,
            ),
            callback=validate_product,
        )

        client.create_job_worker(
            config=WorkerConfig(
                job_type="publish-product",
                job_timeout_milliseconds=30000,
            ),
            callback=publish_product,
        )
        client.create_job_worker(
            config=WorkerConfig(
                job_type="request-product-correction",
                job_timeout_milliseconds=30000,
            ),
            callback=request_product_correction,
        )

        client.create_job_worker(
            config=WorkerConfig(
                job_type="check-seasonal-availability",
                job_timeout_milliseconds=30000,
            ),
            callback=check_seasonal_availability,
        )

        client.create_job_worker(
            config=WorkerConfig(
                job_type="set-product-available",
                job_timeout_milliseconds=30000,
            ),
            callback=set_product_available,
        )

        client.create_job_worker(
            config=WorkerConfig(
                job_type="set-product-unavailable",
                job_timeout_milliseconds=30000,
            ),
            callback=set_product_unavailable,
        )

        client.create_job_worker(
            config=WorkerConfig(
            job_type="send-inventory-update-confirmation",
            job_timeout_milliseconds=30000,
         ),
            callback=send_inventory_update_confirmation,
        )

        await client.run_workers()



if __name__ == "__main__":
    asyncio.run(main())
